-- This code is provided by Quino Terrasa (@espetro)
-- for the 2018 Hacktoberfest BCN

-- To get it running you can call "ghci even_fibonacci_numbers.hs" then "main"
-- or build and run it by "ghc even_fibonacci_numbers.hs"

import Control.Monad

main = do
    putStrLn "Enter the number of test cases followed by them on new lines"
    cases <- getLine
    numbs <- replicateM (read cases) getLine
    let res = map (\x -> sumEvenFib $ read x::Integer) numbs
    mapM_ putStrLn (map show res)
    where
        sumEvenFib x = (sum . filter even . takeWhile (<x)) fib

fib :: Num a => [a]
fib = 0:1: zipWith (+) fib (tail fib)