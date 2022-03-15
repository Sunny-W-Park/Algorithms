//변수 설정: var, let, const 차이


//sort
arr.sort(function(a, b){
    if(a > b){
        return 1;
    }
    else if(a === b){
        return 0;
    }
    else if(a < b){
        return -1;
    }
});
//숫자 오름차순
arr.sort(function(a, b){
    return a - b;
});
//숫자 내림차순
arr.sort(function(a, b){
    return b - a;
});
//문자열 오름차순(유니코드 순서로 정렬, 파라미터 입력x, 대문자가 소문자 앞에 옴)
arr.sort();
//문자열 내림차순
arr.sort(function(a, b){
    if(b > a){
        return 1;
    }
    if(b === a){
        return 0;
    }
    if(b < a){
        return -1;
    }
});
//문자열 오름차순(대소문자 구문 없이)
arr.sort(function(a, b){
    const upperCaseA = a.toUpperCase();
    const upperCaseB = b.toUpperCase();
    if(upperCaseA > upperCaseB){
        return 1;
    }
    else if(upperCaseA === upperCaseB){
        return 0;
    }
    else if(upperCaseA < upperCaseB){
        return -1;
    }
})
//객체 정렬하기(ex. 가격 기준 오름차순)
arr.sort(function(a, b){
    return a.price - b.price;
});


//문자열 match(* 주의: 문자열에서만 검색, 배열은X)
str.match('검색 문자열'); // 검색 문자열이 포함된 단어 출력
//match 정규표현식: .match(/'검색문자'/g): 대소문자 구분 O
//match 정규표현식; .match(/'검색문자'/gi): 대소문자 구분 X
