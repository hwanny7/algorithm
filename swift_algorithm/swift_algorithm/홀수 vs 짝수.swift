import Foundation

func solution(_ num_list:[Int]) -> Int {
    let ans = num_list.enumerated().reduce((even: 0, odd: 0)) { result, tuple in
        let (index, value) = tuple
        if index % 2 == 0 {
            return (result.even + value, result.odd)
        } else {
            return (result.even, result.odd + value)
        }
    }
    return max(ans.even, ans.odd)
}
