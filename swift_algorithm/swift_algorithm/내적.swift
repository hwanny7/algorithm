import Foundation

func solution(_ a:[Int], _ b:[Int]) -> Int {

    return     zip(a, b).reduce(0) { (sum, value) in
        return sum + value.0 * value.1
    }
}
