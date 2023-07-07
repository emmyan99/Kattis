count :: String -> Int
count [] = 0
count ('e':xs) = 1 + count xs
count (_:xs) = count xs

greeting :: Int -> String
greeting x = "h" ++ replicate (x*2) 'e' ++ "y"

main :: IO ()
main = do
    input <- getLine
    let x = count input -- x is number of e in input
        output = greeting x 
    putStrLn output