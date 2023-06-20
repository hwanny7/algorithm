import Foundation

func solution(_ arr:[Int], _ flag:[Bool]) -> [Int] {

    var newArray: [Int] = []

    for (index, bool) in flag.enumerated() {
        if bool {
            newArray = newArray + Array(repeating: arr[index], count: arr[index] * 2)
        } else {
            newArray = Array(newArray[0..<newArray.count - arr[index]])
        }
    }


    return newArray
}
