import pandas as pd
from utils.logger import get_logger

logger = get_logger(__name__)

''' THIS FUNCTION IS DESIGNED TO CLEAN THE DATA , PERFORM FEATURE ENGINERING AND  
    PREPARE IT FOR MODEL TRAINING '''

def preprocess_data(df : pd.DataFrame) -> pd.DataFrame :

    try :
        logger.info("Data Preprocessing started..")

        # CLEANING COLUMN NAMES
        df.columns = [col.strip().replace(" " , '') for col in df.columns]
        logger.info('Cleaned column names')
        logger.info(f"Columns : {df.columns.tolist()}")



        # DROPPING DUPLICATES IF ANY
        initial_rows = df.shape[0]
        final_rows = df.drop_duplicates().shape[0]
        if final_rows < initial_rows :
            df = df.drop_duplicates()
            logger.info(f"Dropped Duplicates. Rows reduced from {initial_rows} to {final_rows}")
        else :
            logger.info("No Duplicate records. No rows dropped")
    

        # DROPPING IRRELEVANT COLUMNS
        if 'CustomerID' in df.columns :
            df = df.drop('CustomerID' , axis = 1)
            logger.info(f"Column dropped: CustomerID. New shape : {df.shape}")
        else :
            logger.info(f"Column not found to drop : 'CustomerID'")
        

        num_cols = df.select_dtypes(exclude = ['object']).columns
        cat_cols = df.select_dtypes(include = ['object']).columns
        logger.info(f"There are {len(num_cols)} numeric columns and {len(cat_cols)} categorical columns")


        # HANDLING MISSING VALUES
        num_cols_with_missing = [col for col in num_cols if df[col].isnull().sum() > 0]
        cat_cols_with_missing = [col for col in cat_cols if df[col].isnull().sum() > 0]

        logger.info(f"There are {len(num_cols_with_missing)} numeric columns with missing values and {len(cat_cols_with_missing)} categorical columns with missing values")

        # FILLING NUMERIC COLUMNS MISSING VALUES 
        for col in num_cols_with_missing :
            df[col] = df[col].fillna(df[col].median())
        
        logger.info("Filled all numeric columns missing values with median values")

        # FILLING CATEGORICAL COLUMNS MISSING VALUES
        for col in cat_cols_with_missing :
            df[col] = df[col].mode()[0]
        
        logger.info("Filled all categorical columns missing values with mode values")

        # CONVERTING NUMERIC COLUMNS TO INT
        for col in num_cols :
            if df[col].dtype != 'int' :
                df[col] = df[col].astype('int')

        logger.info(f"Converted all numeric columns to int")


        # SPECIFIC KNOWN FIXES
        if 'Gender' in df.columns :
            df['Gender'] = df['Gender'].replace('Fe Male' , 'Female')
            logger.info("Fixed 'Fe Male' to 'Female' in Gender column")

        if 'MaritalStatus' in df.columns :
            unique_vals = df['MaritalStatus'].unique().tolist()
            if 'Single' in unique_vals and 'Unmarried' in unique_vals :
                df['MaritalStatus'] = df['MaritalStatus'].replace('Single' , 'Unmarried')
                logger.info("Fixed 'Single' to 'Unmarried' in MaritalStatus column")
            else:
                logger.info("No need to standardize 'MaritalStatus' — consistent values found")

        # MAKING SMALL CATEGORIES AS 'OTHERS'
        threshold = 10
        for col in cat_cols :
            val_counts = df[col].value_counts()
            rare_categories = val_counts[val_counts < threshold].index

            if len(rare_categories) > 0 :
                df[col] = df[col].replace(rare_categories , 'Other')
                logger.info(f"Marked {len(rare_categories)} categories as 'others' in {col} column")
            else :
                logger.info(f"No categories marked as 'others' in {col} column")

        # FEATURE ENGINEERING 
        if 'NumberOfPersonVisiting' in df.columns and 'NumberOfChildrenVisiting' in df.columns :
            df['TotalPersonVisiting'] = df['NumberOfPersonVisiting'] + df['NumberOfChildrenVisiting']
            df['isChildrenVisiting'] = df['NumberOfChildrenVisiting'].apply(lambda x : 1 if x > 0 else 0)
            df = df.drop(['NumberOfPersonVisiting' , 'NumberOfChildrenVisiting'] , axis = 1)

            logger.info("Created 'TotalPersonVisiting' and 'isChildrenVisiting' column and dropped unnecessary columns")
        
        logger.info(f"Data shape after preprocessing : {df.shape}")
        logger.info(f"Columns after preprocessing : {df.columns.tolist()}")

        logger.info("Data Preprocessing completed")

        return df

    except Exception as e :
        logger.exception(f"Error in data preprocessing ")
        raise 




    

        
      
        

        

   
