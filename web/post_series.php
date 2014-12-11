<?php

file_put_contents('php_log', "got here", FILE_APPEND);

if (isset($_POST['data'])) {



    $ipt = str_replace($_POST['data'] , "'");

    file_put_contents('escaped_string', $ipt);

    $result = exec('echo "' . $_POST['data'] . '" | python quickClassify.py')

    file_put_contents('php_result', $result, FILE_APPEND);

    print $result;
}

?>
