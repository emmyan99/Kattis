import Data.List (delete)
import Data.List (isPrefixOf)

readLines :: Int -> [String] -> [String]
readLines n lines = 
    line <- getLine
    readLines (n - 1) (line : lines)

isExit :: String -> [String] -> Bool
isExit line = "exit " `isPrefixOf` line

isEntry :: String -> [String] -> Bool
isEntry line = "entry " `isPrefixOf` line

checkBuildling :: String -> [String] -> Bool
checkBuildling name building = name `elem` buildling

extractName :: String -> String
extractName line
  | isExit = delete "exit " line
  | isEntry = delete "entry " line





createReport :: [String] -> [String] -> String
createReport line buildling


-- ????
applyToLine :: (String -> String) -> [String] -> String
applyToLine _ []     = 0
applyToLine createReport (x:xs) = createReport x + applyToLine createReport xs


main :: IO ()
main = do
    input <- getLine
    let x = read input :: Int
    lines <- readLines x [] -- lines ["entry Abbey", "entry Abbey", "exit Abbey"]

    let building = []
    let output = ""



    --let ans = security lines []
    putStrLn output


--thefunctuin :: [String] -> [String] -> [String]
--thefunctuin [H:T] L = thefunctuin someOther H L



-- behövver på någt sätt loopa genom lines 
-- kolla varje line med isexit, isentry, checkbuilding
-- skapa string eller [string] som blir output och printa på rätt sätt 