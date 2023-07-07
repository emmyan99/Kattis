readLines :: Int -> [String] -> [String]
readLines n lines = 
    line <- getLine
    readLines (n - 1) (line : lines)

checkBuildling :: String -> [String] -> Bool
checkBuildling str building = str `elem` buildling

createReport :: [String] -> [String] -> String
createReport lines buildling
    | -- AAAAA



main :: IO ()
main = do
    input <- getLine
    let x = read input :: Int
    lines <- readLines x [] -- lines ["entry Abbey", "entry Abbey", "exit Abbey"]

    let building = []
    let output = ""

    --let ans = security lines []
    putStrLn output