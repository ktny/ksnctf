<!-- phpのstrcasecmp()には脆弱性がある。
https://www.php.net/manual/ja/function.strcasecmp.php
引数に配列を渡すとnullが返るのでnull == 0で比較するとtrueになってしまう。 -->

<?php
$password = 'FLAG_????????????????';
if (isset($_POST['password']))
    if (strcasecmp($_POST['password'], $password) == 0)
        echo "Congratulations! The flag is $password";
    else
        echo "incorrect...";
?>