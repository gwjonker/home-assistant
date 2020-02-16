# copy files
$source_folder = "/Users/gerwinjonker/devenv/hassio/config"
$dest_folder = "/Volumes/surveillance/hassio/configtest"
$delete_folder = "/Volumes/surveillance/hassio/configtest/.git"

Remove-Item $dest_folder -Recurse -Force

Copy-Item $source_folder -Destination $dest_folder -Recurse -Force 

Remove-Item -Path $delete_folder -Recurse -Force