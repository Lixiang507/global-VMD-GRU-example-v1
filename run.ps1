param([switch]$SelfTest, [string]$Output = '')
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'
$experimentArgs = @((Join-Path $PSScriptRoot 'src\run_experiment.py'))
if ($SelfTest) { $experimentArgs += '--self-test' }
if ($Output) { $experimentArgs += @('--output', $Output) }
& 'E:\Anaconda_lx\envs\dl\python.exe' @experimentArgs
exit $LASTEXITCODE
