<?php

/* This solution offers a function that solves the challenge:
 *
 * This program should read text from a file and stores it in a string until enter 'newline' character is encountered.
 */

/**
 * Returns the first line of a file.
 *
 * @param string $file
 *
 * @throws InvalidArgumentException If given file is not a readable file.
 *
 * @return string
 */
function read_file($file)
{
    if (is_file($file)  === false) {
       throw new \InvalidArgumentException('Given file is not a file');
    } elseif (is_readable($file) === false) {
        throw new \InvalidArgumentException('Given file is not readable');
    } else {
        $lines = file($file);
        $string = reset($lines);

        return $string;
    }
}

echo read_file(__FILE__);
