$days_back = '4'
$file_name = $env:COMPUTERNAME
$folder = 'C:\EventLogs'
$now = Get-Date
$then = (Get-Date).AddDays(-$days_back)

Get-WinEvent -FilterHashtable @{
    LogName = 'Application', 'System';  # Application, System
    Level = 1, 2, 3;  # 1-Critical, 2-Error, 3-Warning
    StartTime = $then;
    EndTime = $now;
} -MaxEvents 1000 | Export-Csv $folder\$file_name-logs.csv

Get-ItemProperty HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* |`
Select-Object -Property DisplayName, DisplayVersion, Publisher, InstallDate `
| Where-Object {
    ($_.PSObject.Properties | ForEach-Object {$_.Value}) -ne $null
} | Export-Csv -Path $folder\$file_name-soft.csv