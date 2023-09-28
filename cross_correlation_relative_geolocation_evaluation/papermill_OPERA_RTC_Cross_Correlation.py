import papermill as pm
from pathlib import Path
import subprocess

# list of paths to OPERA-RTC mosaics on which to run absolute geolocation evaluation
stack_dirs = [
    "path/to/dir/holding/RTC/stack",
]

# True to delete mosaicked RTCs and static files, False to save
delete_mosaics = False

# comment out any file types in cleanup_list that you wish to save
# uncomment those to delete
cleanup_list = (
    # f"{p} amplitude data, "
    # f"flattened {p} amplitude data, "
    # f"flattened and tiled {p} amplitude data, "
    # f"{p} tile correlation results, "
    f", " #don't remove if cleanup list empty
)

output_dirs = [Path.cwd()/f"cross_correlation_{Path(p).name}" for p in stack_dirs]

polarizations = ['vv', 'vh']

for i, d in enumerate(stack_dirs):
    for p in polarizations:
        parameters = {
            "polarization": p,
            "stack_dir": d,
            "delete_mosaics": delete_mosaics,
            "cleanup_list": cleanup_list,     
        }
        output_dirs[i].mkdir(exist_ok=True)
        output = output_dirs[i]/f'output_{Path(d).name}_{p}_OPERA_RTC_Cross_Correlation.ipynb'
        pm.execute_notebook(
            'OPERA_RTC_Cross_Correlation.ipynb',
            output,
            kernel_name='python3',
            parameters = parameters
        )

        subprocess.run([f"jupyter nbconvert {output} --to pdf"], shell=True)  
