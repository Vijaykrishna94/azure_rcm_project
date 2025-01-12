# MAGIC %sql
#--Total Charge Amount per provider by department
# MAGIC CREATE OR REPLACE TABLE gold.amt_provider AS
# MAGIC select
# MAGIC   concat(p.firstname, ' ', p.LastName) Provider_Name,
# MAGIC   dd.Name Dept_Name,
# MAGIC   sum(ft.Amount)
# MAGIC from
# MAGIC   gold.fact_transactions ft
# MAGIC   left join gold.dim_provider p on p.ProviderID = ft.FK_ProviderID
# MAGIC   left join gold.dim_department dd on dd.Dept_Id = p.DeptID
# MAGIC group by
# MAGIC   all ;
# COMMAND ----------
# MAGIC %sql
# --Total Charge Amount per provider by department for each month for year 2024
# MAGIC CREATE OR REPLACE TABLE gold.amt_provider_mnthly_2024 AS
# MAGIC select
# MAGIC   concat(p.firstname, ' ', p.LastName) Provider_Name,
# MAGIC   dd.Name Dept_Name,
# MAGIC   date_format(servicedate, 'yyyyMM') YYYYMM,
# MAGIC   sum(ft.Amount) Total_Charge_Amt,
# MAGIC   sum(ft.paidamount) Total_Paid_Amt
# MAGIC from
# MAGIC   gold.fact_transactions ft
# MAGIC   left join gold.dim_provider p on p.ProviderID = ft.FK_ProviderID
# MAGIC   left join gold.dim_department dd on dd.Dept_Id = p.DeptID
# MAGIC where
# MAGIC   year(ft.ServiceDate) = 2024
# MAGIC group by
# MAGIC   all
# MAGIC order by
# MAGIC   1,
# MAGIC   3;