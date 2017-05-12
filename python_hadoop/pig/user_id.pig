%default INPUT '/user/guan/passwd';
%default OUTPUT '/user/guan/passwdoutput';

A = LOAD '$INPUT' using PigStorage(':');
B = FOREACH A GENERATE $0 as username;
STORE B INTO '$OUTPUT';