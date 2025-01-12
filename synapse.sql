CREATE  VIEW dim_department AS 
SELECT
     Dept_Id,Name
FROM
    OPENROWSET(
        BULK 'https://vjadlsdev.dfs.core.windows.net/gold/dim_department/',
        FORMAT = 'DELTA'
    ) AS [result]




CREATE  VIEW dim_provider AS 
SELECT
     ProviderID,firstname,LastName
FROM
    OPENROWSET(
        BULK 'https://vjadlsdev.dfs.core.windows.net/gold/dim_provider/',
        FORMAT = 'DELTA'
    ) AS [result]

    ;



CREATE  VIEW fact_transactions AS 
SELECT
     FK_ProviderID,Amount,paidamount,servicedate
FROM
    OPENROWSET(
        BULK 'https://vjadlsdev.dfs.core.windows.net/gold/fact_transactions/',
        FORMAT = 'DELTA'
    ) AS [result]
;