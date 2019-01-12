-- Code developed by Quino Terrasa (@espetro) for the
-- 2018 Hacktoberfest BCN

-- run 'ghci reverse_words.hs' then type 'main' to get it working
main = do
    putStrLn "Enter a sentence"
    str <- getLine
    let reversed = (concatMap (++" ") . reverse . words) str
    putStrLn reversed
