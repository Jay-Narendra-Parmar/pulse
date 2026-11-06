Three known gaps in the pulse project 
A timeout still shows a traceback, because ConnectTimeout isn’t caught. Swapping ConnectError for a parent class is a one-line change, so it’s up to you whether to do it now or in Week 2, which covers per-error handling anyway.
The Status: line prints twice.
The security header has only shown not present so far.