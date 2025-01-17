# Revenue Cycle Managment (RCM) 

### Problem Statement : 
	
 	Ensure the Group of Hospitals Provide Quality care while Staying Financially Active  

### Domain : 
	
 	HealthCare

### Objective : 

 	To Build a "Meta Data Driven" (Highly Configurable) Generic ETL Pipeline That Ingests Data From Hospital Database, Processes the Data and Creates Fact and Dimension Tables for Down Stream Teams
 

### Data Sources - 
	EMR Data  (Azure SQL DB) - Table Data 
		- Patients Data
		- Providers(Doctors/Hospitals)
		- Department
		- Transactions 
		- Encounter - Appearances [1 Encounter - Many Transactions]
	Claims Data   - Flat Files -csv -(landing folder) - Monthly once
	NPI Data  - National Provider Identifies - (Public API) 
	ICD Data  - ICD Codes are stadardised systems used by health care providers - map diagnosis code and description. (API)
 
### Tech Stack : Azure SQL DB | ADF | ADLS Gen2 | DataBricks | Delta Lake | Azure Key Vault
  
  #### The Arch Diagram

![image](https://github.com/user-attachments/assets/2d1c08c0-1cb0-47d8-ad43-c5b35f42decd)


  #### Ingestion | ADF
     
  ##### Active Table Pipeline - Reads Config Files to Fetch Active Tables For Ingestion 
     
 ![image](https://github.com/user-attachments/assets/b7980309-4e4b-4742-b5a5-e5a2f9965caf)

  #####  Checks The Type of Load (Full/Incremental Based On Audit Table) and Loads the data Into ADLS Bronze Layer 

![image](https://github.com/user-attachments/assets/03c0600b-7162-4dfb-9213-bcde20fcf10e)

  ### Transformations

  ##### DataBricks ETL 

![image](https://github.com/user-attachments/assets/c20bd83d-7410-4d1f-935e-b891b326f531)

 #### Storage | ADLS

 ##### Containers : Config -  Config Files | Landing - File Uploads | Bronze - Raw Data(Parquet) | Silver - Cleaned Data(Delta Table) [For AI Engineers] | Gold - Fact and Dimension Tables   

![image](https://github.com/user-attachments/assets/f8dbde15-75f2-419f-a17c-f55fd0f58c4c)

 #### Secrets | Azure Key Vault  
    
     SQL DB | ADLS | DATABRICKS(Access Token) Are Registered | registered the Apps (Adf - Adls - Databricks - SqlDB)  
    
    Access Policies 
     
![image](https://github.com/user-attachments/assets/2b829fbb-8edd-4401-9f66-05b718a3ba45)

  
 

  
      
     
 

