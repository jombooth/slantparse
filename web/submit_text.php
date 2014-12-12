<?php

//file_put_contents('php_log', "got here", FILE_APPEND);

if (isset($_POST['data'])) {

    if (strlen($_POST['data']) < 100) {
        print "Input string was below the 100 character minimum!";
        die();
    }
    else if (strlen($_POST['data']) > 10000000) {
        print "Query larger than 1MB. Dying.";
        die();
    }
    // $_POST['data'] = "George dubya \" sure bunged up this one";
    $ipt = str_replace('"', "'", $_POST['data']);

    file_put_contents('escaped_string', $ipt);

    $query = 'echo "' . $ipt . '" | python quickClassify.py';

    $result = exec($query);

    file_put_contents('php_query', $query);
    file_put_contents('php_result', $result);

    print $result;
}

?>
