import Foundation

func solution(_ sizes:[[Int]]) -> Int {

    let num: (Int, Int) = sizes.reduce((maxNum: 0, minNum: 0)) { (sum, value) in
        return (max(sum.maxNum, max(value[0], value[1])), max(sum.minNum, min(value[0], value[1])))
    }

    return num.0 * num.1
}
