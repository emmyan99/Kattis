import Data.List.Split (splitOn)

count :: String -> Int
count [] = 0
count ('|':xs) = 1 + count xs
count (_:xs) = count xs

check :: Int -> Int -> String
check x y
    | x == y = "correct"
    | otherwise = "fix"

main :: IO ()
main = do
    input <- getLine
    let [left, right] = splitOn "()" input
    let x = count left
    let y = count right
        ans = check x y
    putStrLn ans