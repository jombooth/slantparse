<?php

include_once("config.php");

file_put_contents('php_log', "got here", FILE_APPEND);

if (isset($_POST['user_agent']) && isset($_POST['time_series'])) {
    $user_agent = mysql_real_escape_string($_POST['user_agent']);
    $time_series = mysql_real_escape_string($_POST['time_series']);
    file_put_contents('php_log_query', $user_agent);
    //file_put_contents('php_log_query', $time_series, FILE_APPEND);
    $qs = "INSERT INTO ts_table (UserAgent, TimeSeries) VALUES (\"" + $user_agent + "\", \"" + $time_series + "\")";

    //file_put_contents('php_log_query', $qs, FILE_APPEND);

    $mysqli->query($qs);
    $mysqli->close();
}

?>
