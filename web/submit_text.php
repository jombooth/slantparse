<?php

if (isset($_POST['data'])) {
    if (strlen($_POST['data']) < 1000) {
        print "Input string was below the 1000 character minimum!";
        die();
    }
    else if (strlen($_POST['data']) > 10000000) {
        print "Query larger than 1MB. Dying.";
        die();
    }
    else {
        $ipt = str_replace('"', "'", $_POST['data']);
        $query = 'echo "' . $ipt . '" | python quickClassify.py';
        $result = exec($query);
        print $result;
    }
}

?>
