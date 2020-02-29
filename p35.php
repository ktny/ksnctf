<!-- http://ctfq.sweetduet.info:10080/~q35/database.db でファイルをダウンロード
sqlite3 database.db でDBにログイン
select * from user; -->

<?php
$try = false;
$ok = false;

if ($_POST['id']!=='' or $_POST['password']!=='')
{
    $try = true;
    // sqlite:database.dbという指定は相対パスなのでdatabase.dbファイルの場所がわかる
    $db = new PDO('sqlite:database.db');
    $s = $db->prepare('SELECT * FROM user WHERE id=? AND password=?');
    $s->execute(array($_POST['id'], $_POST['password']));
    $ok = $s->fetch() !== false;
}
?>