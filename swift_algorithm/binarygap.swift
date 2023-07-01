import Foundation


// you can write to stdout for debugging purposes, e.g.
// print("this is a debug message")

public func solution(_ N : Int) -> Int {
    var indexArray: [Int] = []
    var ans:Int = 0

    for (index, char) in String(N, radix: 2).enumerated() where char == "1" {
        indexArray.append(index)
    }

    if indexArray.count >= 2 {
        for index in 0..<indexArray.count - 1 {
            ans = max(ans, indexArray[index + 1] - indexArray[index] - 1)
        }
    }


    return ans
}

