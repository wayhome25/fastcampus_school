# sass

- Syntatically Awesome Stylesheet
- CSS 전처리기 (Pre-Processor)
	- Sass와 같은 'css 확장 언어'의 파일을 웹 브라우저에서 해석할 수 있는 css 파일로 만들어주는 처리기

## sass 기본구조

```css
div.container {
	padding: 15px;
	margin: 0;

	> p#main-title {
		font-size: 16px;
		font-weight: bold;
	}

	> .fixed {
		position: fixed;
		bottom: 10px;
	}
}
```

## sass의 출력 스타일
- expanded : 일반적인 css 스타일
- nested : 부모자식 관계를 들여쓰기로 구분
- compact : 선택자마다 1줄 씩 차지
- compreseed : min 형식으로 압축

## sass-autocompile
- `sass-autocompile` : atom 에서 sass를 보다 편리하게 사용하기 위한 패키지

### 설정
- compile with '저장방식' : 어떤 방식으로 저장할 것인지 지정
- css 파일 저장 경로는 상대 경로로 지정 ('../css/')

---

# sass 문법

## 주석

```css
// 주석내용
/* 주석내용 여러줄 작성 가능*/ (css기본)
```

## 중첩 (Nested)

```css
.container {
	width: 100px

	/*.container > #page 의미*/
	> #page {
		padding: 10px;

		/*.container > #page p.section-title 의미*/
		p.section-title {
			font-size: 20px;
		}
	}
}
```

## 부모 참조 선택자 (&)

```css
#page{
	width: 800px;

	a {
		text-decoration: none;

 		/*&은 자신의 부모 선택자 참조*/
		&:hover {
			color: red;
		}

		/*  & 앞에 선택자가 있을 경우,
			해당 선택자 다음에 현재 위치에서의 부모 선택자를 참고 */
		.link-container & {
			font-size: 30px;
		}
	}
}
```

## 중첩 속성

## 선택자 상속 (@extend)

```css
.btn {
	font-weight: bold;  
	color: white;  
	padding: 5px 20px;  
}

.btn-cancel {
	@extend .btn;
	color: rend;
}
```

## 대체 선택자 (%) - placeholer selector
- %btn에 지정한 속성은 css에서 나타나지 않는다

```css
%btn {
	font-weight: bold;  
	color: white;  
	padding: 5px 20px;  
}

.btn-cancel {
	@extend .btn;
	color: rend;
}
```
## 변수($)

```css
/*_variables.scss*/

$padding: 10px;
$bg-color:#fff
$title-font-weight:bold;

div.container{
	background-color: $bg-color;
	padding: padding;

	p#main-title {
		font-weight: $title-font-weight;
	}
}
```

## sass 파일 호출
- css 파일을 불러올 때는 확장자를 입력하여야 하지만, sass 파일을 불러올 때는 확장자를 입력하지 않아도 된다
- `_(underscore)`로 시작하는 파일은 css파일로 컴파일 되지 않는다.
- import시에만 사용하는 파일은 `_`를 붙여서 네이밍 한다
```css
/*현재 파일 위치를 기준으로 불러온다*/
@import 'variables'

.btn{
	background-color: $bg-color;
}

```
