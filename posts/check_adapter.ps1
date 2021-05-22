# Part of project - get adapter details

$IPType = 'IPv4'
$Adapter = Get-NetAdapter | Where-Object Status -EQ 'Up'
$Interface = $Adapter | Get-NetIPInterface -AddressFamily $IPType
$Index = $Interface.ifIndex
Get-NetIPAddress -InterfaceIndex $Index -AddressFamily $IPType |
Format-Table -Property Interface*, IPAddress, PrefixLength


$IPHT = @{
    InterfaceIndex = $Index
    PrefixLength = 24
    IPAddress = '10.10.10.51'
    DefaulGateway = '10.10.10.254'
    AddressFamily = $IPType
}
New-NetIPAddress @IPType | Out-Null