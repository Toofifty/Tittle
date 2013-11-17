ECHO OFF
for /r %%G in (*.py) do (
busybox grep . "%%G" | busybox wc -l
) 
pause