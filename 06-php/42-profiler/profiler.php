<?php

require_once __DIR__ . '/profiler-includes.php';

for ($i = 0; $i < 30; $i++) {
    $functionName = 'f' . rand(1, 3);
    $functionName();
}

/*
[XDebug]
xdebug.mode=profile
xdebug.start_with_request=yes
xdebug.output_dir=C:\Users\artur\workspace\ptw\06-php\profiler
xdebug.profiler_output_name=cachegrind.out.%p
*/
