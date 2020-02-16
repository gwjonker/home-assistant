Set-ExecutionPolicy -ExecutionPolicy Unrestricted

$Path = "C:\Users\gwjon\Dropbox\Apps\HassioRpi2-backups\HassioRpi2-backups"
$Daysback = "-14"
$NamePattern = "*.tar"

$CurrentDate = Get-Date
$DateToDelete = $CurrentDate.AddDays($Daysback)

$FolderSizeBefore = [math]::Round((Get-ChildItem $Path -Recurse | Measure-Object -Property Length -Sum -ErrorAction Stop).Sum / 1GB, 2)
$FolderSizeToDelete = [math]::Round((Get-ChildItem $Path -Recurse | Where-Object { $_.LastWriteTime -lt $DateToDelete } | ?{$_.Name -like $NamePattern} | Measure-Object -Property Length -Sum -ErrorAction Stop).Sum / 1GB, 2)


"Folder size before:     {0} GB" -f $FolderSizeBefore
"Delete files days back: {0} days" -f $Daysback
"All files before:       {0}" -f $DateToDelete
"Name pattern to delete: {0}" -f $NamePattern
"Folder size to delete:  {0} GB" -f $FolderSizeToDelete

"Deleting files {0}..." -f $NamePattern
Get-ChildItem $Path -Recurse | Where-Object { $_.LastWriteTime -lt $DateToDelete } | ?{$_.Name -like $NamePattern} | Remove-Item

$FolderSizeAfter = [math]::Round((Get-ChildItem $Path -Recurse | Measure-Object -Property Length -Sum -ErrorAction Stop).Sum / 1GB, 2)
"Folder size after:      {0} GB" -f $FolderSizeAfter


