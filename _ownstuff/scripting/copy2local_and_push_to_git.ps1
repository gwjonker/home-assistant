# copy files
$source_folder = "/Volumes/surveillance/hassio/config"
$dest_folder = "/Users/gerwinjonker/devenv/hassio"
$git_folder = $dest_folder + "/config"

Copy-Item $source_folder -Destination $dest_folder -Recurse -Force 



cd $git_folder

git add .

git commit -m "auto update"

git push