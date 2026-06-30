# Personal Finance Planner

한국 거주자를 위한 개인 재무관리 Claude Skill입니다.

`Personal Finance Planner`는 Claude에서 사용할 수 있는 개인 재무관리용 Skill로, 사용자의 수입, 지출, 자산, 부채, 투자, 연금, 주거, 세금 관련 정보를 구조화해 **예산 관리, 부채 상환, 순자산 정리, 투자 배분 점검, 은퇴 계획, 주거 판단, 세금 체크, 재무 건강점수 산출**을 도와줍니다.

이 Skill은 금융상품을 대신 가입해주거나, 투자를 실행하거나, 세금 신고를 대행하는 도구가 아닙니다.  
사용자가 직접 입력한 정보를 바탕으로 재무 상황을 정리하고, 의사결정에 참고할 수 있는 교육용 분석과 실행 계획을 제공합니다.

---

## 주요 목적

많은 사람들은 돈 관리를 하려고 해도 어디서부터 정리해야 할지 모릅니다.

월급은 들어오지만 카드값이 왜 이렇게 나가는지 모르고,  
대출을 먼저 갚아야 할지 투자를 해야 할지 헷갈리고,  
ISA, 연금저축, IRP, 퇴직연금, 국민연금, 청약, 전세대출 같은 제도는 이름만 들어도 복잡합니다.

`Personal Finance Planner`는 이런 질문을 Claude와 함께 단계적으로 정리할 수 있도록 설계되었습니다.

예를 들어 다음과 같은 상황에서 사용할 수 있습니다.

- 월급 관리를 시작하고 싶을 때
- 고정비와 변동비를 정리하고 싶을 때
- 카드값, 신용대출, 전세대출, 주택담보대출을 어떻게 관리할지 고민될 때
- 내 순자산이 얼마인지 한눈에 보고 싶을 때
- 투자 비중이 너무 공격적인지, 너무 보수적인지 점검하고 싶을 때
- ISA, 연금저축, IRP, 퇴직연금 계좌를 어떻게 나눠 써야 할지 고민될 때
- 국민연금과 개인연금을 포함해 노후 준비 상태를 확인하고 싶을 때
- 전세, 월세, 매매, 청약 중 어떤 선택이 현재 상황에 맞는지 비교하고 싶을 때
- 프리랜서, 개인사업자, 직장인으로서 세금 체크포인트를 정리하고 싶을 때
- 조기은퇴 또는 FIRE 가능성을 계산해보고 싶을 때
- 매월 내 재무 상태를 점검하고 싶을 때

---

## 이 Skill이 하는 일

`Personal Finance Planner`는 사용자의 재무 정보를 바탕으로 다음 작업을 수행합니다.

### 개인 재무 프로필 생성

사용자의 기본 상황을 정리합니다.

- 나이대
- 직업 및 소득 형태
- 가족상황
- 주거형태
- 월 실수령액 또는 월평균 소득
- 고정비
- 변동비
- 자산
- 부채
- 보험
- 연금
- 투자 현황
- 단기/중기/장기 목표

생성되는 파일 예시:

```txt
1-my-profile.md
```

---

### 월 예산 분석

수입과 지출을 기준으로 월별 예산 상태를 분석합니다.

분석 항목은 다음과 같습니다.

- 월 실수령액
- 고정비 비율
- 변동비 비율
- 저축률
- 투자율
- 구독비
- 카드값
- 주거비 부담
- 보험료 부담
- 생활비 누수 구간
- 이번 달 줄일 수 있는 지출 항목

생성되는 파일 예시:

```txt
2-my-budget.md
```

---

### 전체 재무 계획 생성

사용자의 목표와 현재 상황을 바탕으로 실행 가능한 계획을 만듭니다.

포함되는 내용은 다음과 같습니다.

- 현재 재무 상태 요약
- 가장 먼저 해결해야 할 문제
- 부채 상환 우선순위
- 비상금 목표
- 투자 배분 점검
- 연금 준비 방향
- 주거 관련 체크포인트
- 세금 관련 확인 항목
- 30일, 60일, 90일 액션 플랜
- 장기 목표별 실행 방향

생성되는 파일 예시:

```txt
3-my-plan.md
```

---

### HTML 대시보드 생성

재무 상태를 시각적으로 확인할 수 있는 대시보드를 생성합니다.

포함 가능한 항목은 다음과 같습니다.

- 순자산
- 총자산
- 총부채
- 저축률
- 부채비율
- 투자 비중
- 현금 비중
- 은퇴 준비도
- 재무 건강점수
- 주요 리스크
- 이번 달 액션

생성되는 파일 예시:

```txt
4-my-dashboard.html
```

---

### 월간 체크인

한 번 계획을 만든 뒤에도 계속 업데이트할 수 있습니다.

예를 들어 다음과 같이 물어볼 수 있습니다.

```txt
이번 달 체크인 하자.
```

```txt
이번 달 카드값이 늘었는데 계획 다시 봐줘.
```

```txt
월급이 올랐어. 예산 다시 계산해줘.
```

```txt
전세대출이 생겼어. 부채 계획 업데이트해줘.
```

체크인 결과는 다음 폴더에 저장됩니다.

```txt
check-ins/
```

---

## 이 Skill이 하지 않는 일

이 프로젝트는 안전한 사용을 위해 다음을 하지 않습니다.

- 금융상품 가입을 대신하지 않습니다.
- 주식, ETF, 코인 등의 매수/매도 지시를 하지 않습니다.
- 특정 종목이나 상품의 수익을 보장하지 않습니다.
- 세금 신고 결과를 확정하지 않습니다.
- 대출 가능 여부를 확정하지 않습니다.
- 보험 가입 또는 해지를 단정적으로 지시하지 않습니다.
- 법률, 세무, 투자, 보험 자문을 전문가처럼 제공하지 않습니다.
- 은행 계좌, 증권 계좌, 카드 계좌에 직접 접속하지 않습니다.
- 주민등록번호, 계좌번호, 카드번호, 비밀번호, 인증번호를 요구하지 않습니다.

이 Skill은 입력값을 바탕으로 한 **정보 제공 및 교육 목적의 재무관리 보조 도구**입니다.

중요한 의사결정 전에는 금융전문가, 세무사, 회계사, 법률전문가, 보험전문가 등 관련 전문가와 상담해야 합니다.

---

## 지원 명령어

아래 명령어를 통해 기능별 분석을 실행할 수 있습니다.

```txt
/finance
```

전체 재무 계획을 시작하거나 기존 계획을 불러옵니다.

---

```txt
/finance quick
```

빠른 재무 진단을 실행합니다.  
월 실수령액, 월 지출, 총자산, 총부채, 월 저축액 정도만 입력해도 간단한 점검이 가능합니다.

---

```txt
/finance budget
```

예산과 현금흐름을 분석합니다.

주요 분석 항목:

- 월 수입
- 월 지출
- 고정비
- 변동비
- 저축률
- 투자율
- 생활비 누수
- 구독비 점검
- 카드값 위험도

---

```txt
/finance debt
```

부채 상환 전략을 정리합니다.

지원 가능한 부채 예시:

- 신용대출
- 카드론
- 리볼빙
- 자동차 할부
- 학자금대출
- 전세대출
- 주택담보대출
- 개인 간 차용금

분석 예시:

- 금리 높은 순 상환
- 잔액 작은 순 상환
- 월 상환 가능액
- 예상 상환 기간
- 이자 부담
- 부채 위험도

---

```txt
/finance networth
```

순자산을 계산합니다.

계산 구조:

```txt
순자산 = 총자산 - 총부채
```

정리 가능한 항목:

- 현금
- 예금
- 적금
- CMA
- 파킹통장
- 국내주식
- 해외주식
- ETF
- 펀드
- 코인
- 전세보증금
- 부동산
- 자동차
- 대출
- 카드값
- 할부금

---

```txt
/finance invest
```

투자 배분을 점검합니다.

분석 항목:

- 현금 비중
- 예금/적금 비중
- 국내주식 비중
- 해외주식 비중
- ETF 비중
- 연금계좌 비중
- 코인 비중
- 위험자산 비중
- 목표 기간별 적정성
- 리밸런싱 필요 여부

개별 종목 매수/매도 추천은 하지 않습니다.

---

```txt
/finance retirement
```

은퇴 준비 상태를 점검합니다.

분석 항목:

- 국민연금
- 퇴직연금
- 연금저축
- IRP
- 개인 투자자산
- 예상 은퇴 생활비
- 은퇴 필요자금
- 부족 자금
- 월 추가 저축 필요액

---

```txt
/finance fire
```

FIRE, 즉 경제적 자유 또는 조기은퇴 가능성을 계산합니다.

분석 항목:

- 현재 월 생활비
- 예상 은퇴 후 월 생활비
- 연 생활비
- 목표 인출률
- 필요 순자산
- 현재 저축률 기준 예상 도달 시점
- 보수/중립/공격 시나리오

---

```txt
/finance housing
```

주거 관련 선택지를 비교합니다.

분석 가능한 주제:

- 월세 vs 전세
- 전세 vs 매매
- 청약 대기 vs 매수
- 전세대출 부담
- 주택담보대출 부담
- 주거비 적정성
- 이사 가능성
- 생애최초, 신혼부부, 청년 관련 제도 확인 항목

실제 대출 가능 여부와 정책 대상 여부는 금융기관 및 공식 기관 확인이 필요합니다.

---

```txt
/finance tax
```

세금 관련 체크포인트를 정리합니다.

대상별 분석:

- 직장인
- 프리랜서
- 개인사업자
- 부업 소득자
- 투자 소득자

체크 항목:

- 연말정산
- 종합소득세
- 3.3% 원천징수
- 필요경비
- 부가세
- 연금저축 세액공제
- IRP 세액공제
- 금융소득종합과세
- 해외주식 양도소득세
- 건강보험료 영향

세무 판단은 개인 상황에 따라 달라질 수 있으므로, 확정 신고 전에는 세무 전문가와 확인해야 합니다.

---

```txt
/finance compare
```

두 선택지를 비교합니다.

예시:

```txt
/finance compare 전세 유지 vs 월세 이사
```

```txt
/finance compare 대출 먼저 갚기 vs 투자하기
```

```txt
/finance compare 퇴사 후 프리랜서 vs 직장 유지
```

```txt
/finance compare 자동차 구매 vs 대중교통 유지
```

비교 기준:

- 초기 비용
- 월 현금흐름
- 리스크
- 되돌릴 수 있는지
- 세금 영향
- 심리적 부담
- 장기 목표와의 적합성

---

```txt
/finance report
```

전체 리포트를 생성합니다.

생성 가능한 결과물:

- Markdown 리포트
- HTML 대시보드
- 선택적 PDF 리포트

---

## 재무 건강점수

이 Skill은 사용자의 입력값을 기준으로 100점 만점의 재무 건강점수를 계산합니다.

점수는 다음 6개 영역을 기준으로 합니다.

| 영역 | 배점 | 설명 |
|---|---:|---|
| 현금흐름 / 예산 관리 | 20점 | 수입 대비 지출, 저축률, 예산 안정성 |
| 부채 안정성 | 20점 | 총부채, 금리, 상환 부담, 연체 위험 |
| 비상금 / 보호장치 | 15점 | 비상금, 보험, 소득공백 대비 |
| 투자 / 자산배분 | 15점 | 현금·투자·연금 비중과 위험도 |
| 연금 / 은퇴준비 | 15점 | 국민연금, 퇴직연금, 연금저축, IRP 등 |
| 주거 / 세금 / 제도 활용 | 15점 | 주거비 부담, 세금 체크, 제도 활용 가능성 |

등급 기준은 다음과 같습니다.

| 점수 | 등급 | 의미 |
|---:|---|---|
| 85–100 | Excellent | 전반적으로 안정적이며 일부 최적화 중심 |
| 70–84 | Healthy | 양호하지만 개선할 영역이 있음 |
| 55–69 | Watch | 관리가 필요한 항목이 여러 개 있음 |
| 40–54 | Weak | 현금흐름, 부채, 비상금 중 우선 정리가 필요함 |
| 0–39 | Critical | 연체, 과도한 부채, 비상금 부족 등 즉시 점검 필요 |

점수는 사용자를 평가하기 위한 목적이 아닙니다.  
현재 상태를 한눈에 보고, 어떤 영역부터 개선해야 할지 우선순위를 잡기 위한 참고 지표입니다.

---

## 생성되는 파일

이 Skill을 사용하면 작업 폴더에 다음 파일이 생성될 수 있습니다.

```txt
1-my-profile.md
2-my-budget.md
3-my-plan.md
4-my-dashboard.html
check-ins/
shareable/
README.txt
```

### `1-my-profile.md`

사용자의 재무 기본 정보를 저장합니다.

예시:

```md
# My Financial Profile

## Basic Info

- Age Range: 30s
- Employment Type: Employee + Side Income
- Housing: Jeonse
- Household: Single

## Income

- Monthly Take-Home Pay: 3,200,000 KRW
- Side Income: 500,000 KRW

## Goals

- Build emergency fund
- Reduce credit card spending
- Start retirement savings
- Prepare for housing decision
```

---

### `2-my-budget.md`

월별 예산과 지출 구조를 저장합니다.

예시:

```md
# Monthly Budget

## Income

- Salary: 3,200,000 KRW
- Side Income: 500,000 KRW
- Total: 3,700,000 KRW

## Expenses

- Housing: 800,000 KRW
- Food: 600,000 KRW
- Transportation: 120,000 KRW
- Insurance: 180,000 KRW
- Subscriptions: 80,000 KRW
- Variable Spending: 700,000 KRW

## Summary

- Total Expenses: 2,480,000 KRW
- Monthly Surplus: 1,220,000 KRW
- Savings Rate: 32.9%
```

---

### `3-my-plan.md`

전체 실행 계획을 저장합니다.

예시:

```md
# Personal Finance Plan

## Top Priorities

1. Build emergency fund to 3 months of essential expenses
2. Reduce high-interest debt first
3. Separate short-term cash and long-term investment money
4. Review pension account contributions
5. Check housing decision within 6 months

## 90-Day Plan

### Days 1–30

- Track all expenses
- Cancel unused subscriptions
- Set emergency fund target
- List all debts with interest rates

### Days 31–60

- Start automated savings
- Review ISA and pension account options
- Create debt payoff plan

### Days 61–90

- Rebalance cash/investment ratio
- Review housing timeline
- Prepare tax-related documents
```

---

### `4-my-dashboard.html`

브라우저에서 열 수 있는 시각화 대시보드입니다.

포함 가능한 요소:

- 재무 건강점수
- 순자산 그래프
- 자산/부채 구성
- 월 현금흐름
- 저축률
- 부채 상환 진행률
- 은퇴 준비도
- 이번 달 액션

---

## 사용 예시

### 예시 1. 처음 시작하기

Claude에서 다음과 같이 입력합니다.

```txt
내 돈 관리 도와줘.
```

또는

```txt
/finance
```

그러면 Claude가 한 번에 모든 정보를 요구하지 않고, 단계별로 질문합니다.

예상 질문:

```txt
먼저 기본 상황부터 정리할게.

1. 나이대가 어떻게 돼?
2. 직업/소득 형태는 뭐야? 예: 직장인, 프리랜서, 개인사업자, 학생 등
3. 월 실수령액 또는 월평균 소득은 어느 정도야?
4. 지금 제일 해결하고 싶은 문제는 예산, 대출, 투자, 주거, 은퇴, 세금 중 뭐에 가까워?
```

---

### 예시 2. 빠른 진단

```txt
/finance quick
```

입력 예시:

```txt
월 실수령액 320만원
월 지출 250만원
현금성 자산 600만원
투자금 900만원
총부채 1200만원
월 저축 가능액 50만원
나이는 32세
목표는 2년 안에 전세 이사
```

예상 출력:

```md
## 빠른 재무 진단

현재 입력값 기준 재무 건강점수는 64점입니다.

### 좋은 점

- 월 저축 가능액이 있습니다.
- 현금성 자산이 완전히 부족한 상태는 아닙니다.
- 목표 기간이 2년으로 비교적 명확합니다.

### 주의할 점

- 총부채가 현금성 자산보다 큽니다.
- 전세 이사 목표가 있다면 현금 비중을 더 높여야 합니다.
- 투자금과 주거 목표 자금을 분리해서 관리할 필요가 있습니다.

### 이번 달 액션

1. 부채별 금리와 만기를 정리합니다.
2. 전세 이사용 자금 계좌를 따로 분리합니다.
3. 월 고정비 중 10만원 이상 줄일 항목을 찾습니다.
```

---

### 예시 3. 대출 상환 전략

```txt
/finance debt
```

입력 예시:

```txt
신용대출 700만원, 금리 7.2%
카드론 250만원, 금리 13.5%
자동차 할부 500만원, 금리 5.8%
월 추가 상환 가능액은 60만원
```

예상 출력:

```md
## 부채 상환 전략

입력값 기준으로는 카드론을 가장 먼저 정리하는 것이 이자 부담을 줄이는 데 유리합니다.

### 부채 목록

| 부채 | 잔액 | 금리 | 우선순위 |
|---|---:|---:|---:|
| 카드론 | 2,500,000원 | 13.5% | 1 |
| 신용대출 | 7,000,000원 | 7.2% | 2 |
| 자동차 할부 | 5,000,000원 | 5.8% | 3 |

### 권장 방향

- 최소상환액은 모두 유지합니다.
- 추가 상환 가능액 60만원은 카드론에 우선 투입합니다.
- 카드론 상환 후 같은 금액을 신용대출로 이동합니다.
- 자동차 할부는 금리가 상대적으로 낮으므로 마지막 순위로 둡니다.
```

---

### 예시 4. 전세 vs 월세 비교

```txt
/finance compare 전세 유지 vs 월세 이사
```

입력 예시:

```txt
현재 전세보증금 2억
전세대출 1억, 금리 4.1%
월세로 가면 보증금 3000만원, 월세 90만원
월 실수령액은 350만원
현금성 자산은 2000만원
```

예상 출력:

```md
## 전세 유지 vs 월세 이사 비교

### 1. 월 현금흐름

| 선택지 | 월 고정 주거비 | 특징 |
|---|---:|---|
| 전세 유지 | 대출이자 중심 | 월세보다 현금흐름 부담이 낮을 수 있음 |
| 월세 이사 | 월세 90만원 | 매월 고정 지출 증가 |

### 2. 유동성

월세로 이동하면 전세보증금 일부가 현금화될 수 있지만, 매월 고정비가 증가합니다.

### 3. 리스크

- 전세 유지: 금리 상승, 보증금 반환 리스크 확인 필요
- 월세 이사: 월 고정비 증가, 저축률 하락 가능성

### 4. 현재 입력값 기준 방향

현금흐름만 보면 전세 유지가 유리할 가능성이 있습니다.  
다만 전세보증금 안정성, 대출 만기, 금리 변동, 이사 계획을 함께 확인해야 합니다.
```

---

## 민감정보 입력 금지

다음 정보는 절대 입력하지 마세요.

```txt
주민등록번호
계좌번호 전체
카드번호 전체
비밀번호
인증번호
공동인증서 정보
신분증 이미지
계좌 로그인 정보
카드 CVC
정확한 주소
```

필요한 경우에는 숫자를 둥글게 입력하는 것을 권장합니다.

예:

```txt
월 실수령액 약 320만원
신용대출 약 700만원
월세 약 80만원
투자금 약 1000만원
```

---

## 한국형 제도 관련 주의사항

한국의 금융, 세금, 연금, 주거 관련 제도는 자주 바뀔 수 있습니다.

따라서 다음 항목은 최신 공식 자료 확인이 필요합니다.

- ISA 납입한도 및 비과세 한도
- 연금저축 세액공제 한도
- IRP 세액공제 한도
- 국민연금 기준소득월액
- 건강보험료 기준
- 금융소득종합과세 기준
- 해외주식 양도소득세 기본공제
- 청약 제도
- 디딤돌대출, 버팀목대출, 보금자리론 조건
- DSR, LTV, DTI 규제
- 예금자보호 한도
- 주택 관련 세금
- 프리랜서 및 개인사업자 세금 기준

이 Skill은 제도 정보를 참고용으로 정리할 수 있지만, 최신성과 개인별 적용 여부는 반드시 공식 기관 또는 전문가를 통해 확인해야 합니다.

---

## 권장 첫 프롬프트

처음 사용할 때는 아래 문장으로 시작하면 됩니다.

```txt
내 돈 관리 도와줘.
```

조금 더 자세히 시작하고 싶다면 다음처럼 입력할 수 있습니다.

```txt
나는 한국 거주자고, 월급 관리와 대출 상환, 투자 비중을 같이 정리하고 싶어. 
한 번에 너무 많이 묻지 말고 단계별로 질문해줘.
```

또는 빠른 진단을 원한다면:

```txt
/finance quick

월 실수령액:
월 지출:
현금성 자산:
투자금:
총부채:
월 저축 가능액:
나이:
가장 중요한 목표:
```

---

## 설치 및 사용

이 저장소를 Claude Skill 폴더에 추가한 뒤 사용할 수 있습니다.

예시:

```bash
git clone https://github.com/loo8ight/personal-finance-planner.git
```

Claude Code에서 사용할 경우, 사용자의 환경에 맞게 Skill 폴더에 복사한 뒤 실행합니다.

예시:

```bash
mkdir -p ~/.claude/skills
cp -R personal-finance-planner ~/.claude/skills/personal-finance-planner
```

그다음 Claude Code에서 작업 폴더를 열고 다음과 같이 입력합니다.

```txt
/finance
```

또는:

```txt
내 돈 관리 도와줘.
```

---

## 프로젝트 구조

```txt
personal-finance-planner/
├── README.md
├── LICENSE
├── NOTICE.md
├── SKILL.md
├── commands/
│   ├── finance.md
│   ├── finance-quick.md
│   ├── finance-budget.md
│   ├── finance-debt.md
│   ├── finance-networth.md
│   ├── finance-invest.md
│   ├── finance-retirement.md
│   ├── finance-fire.md
│   ├── finance-housing.md
│   ├── finance-tax.md
│   ├── finance-compare.md
│   └── finance-report.md
├── references/
│   ├── interview-guide.md
│   ├── korea-finance-rules.md
│   ├── korea-tax-basics.md
│   ├── korea-accounts.md
│   ├── pension-retirement.md
│   ├── housing-cheongyak-loans.md
│   ├── debt-strategy.md
│   ├── investment-basics.md
│   ├── insurance-protection.md
│   ├── freelancer-business-tax.md
│   ├── life-events.md
│   ├── calculations-dashboard.md
│   └── disclaimers.md
├── templates/
│   ├── profile-template.md
│   ├── budget-template.md
│   ├── plan-template.md
│   ├── dashboard-template.html
│   ├── monthly-checkin-template.md
│   └── report-template.md
├── scripts/
│   ├── budget_calculator.py
│   ├── debt_payoff.py
│   ├── networth_calculator.py
│   ├── finance_score.py
│   ├── retirement_projection.py
│   ├── fire_calculator.py
│   ├── housing_affordability.py
│   └── generate_report.py
└── examples/
    ├── sample-profile.md
    ├── sample-budget.md
    ├── sample-plan.md
    └── sample-dashboard.html
```

---

## 개발 방향

이 프로젝트는 다음 원칙을 따릅니다.

### 1. 숫자 중심

가능하면 감정적인 조언보다 숫자 기반 분석을 우선합니다.

예:

```txt
지출이 많아요.
```

보다:

```txt
월 실수령액 대비 고정비 비율이 52%입니다. 
주거비와 보험료를 먼저 점검하면 저축률 개선 가능성이 큽니다.
```

---

### 2. 실행 중심

분석에서 끝나지 않고, 사용자가 실제로 할 수 있는 행동으로 연결합니다.

예:

```txt
이번 달 실행할 액션

1. 최근 3개월 카드명세서에서 반복 결제 항목을 확인한다.
2. 대출별 금리와 만기를 한 표로 정리한다.
3. 비상금 목표를 월 필수지출의 3개월치로 설정한다.
```

---

### 3. 안전한 표현

투자, 세금, 대출, 보험과 관련된 내용은 단정하지 않습니다.

사용하는 표현:

```txt
현재 입력값 기준으로는
가정이 맞다면
확인이 필요한 항목은
전문가 상담이 필요한 구간은
최신 공식 자료 확인이 필요합니다
```

사용하지 않는 표현:

```txt
무조건 사세요
반드시 가입하세요
이 상품이 제일 좋습니다
수익 보장됩니다
세금 안 냅니다
대출 무조건 됩니다
```

---

## 예시 리포트 구조

`/finance report` 실행 시 다음과 같은 리포트가 생성될 수 있습니다.

```md
# Personal Finance Report

## 1. 요약

- 재무 건강점수: 68점
- 현재 상태: 관리 필요
- 가장 큰 강점: 월 저축 가능액 존재
- 가장 큰 리스크: 비상금 부족과 고금리 부채
- 최우선 액션: 카드론 상환과 비상금 분리

## 2. 현금흐름

| 항목 | 금액 |
|---|---:|
| 월 실수령액 | 3,500,000원 |
| 월 고정비 | 1,500,000원 |
| 월 변동비 | 900,000원 |
| 월 저축 가능액 | 1,100,000원 |
| 저축률 | 31.4% |

## 3. 부채

| 부채 | 잔액 | 금리 | 우선순위 |
|---|---:|---:|---:|
| 카드론 | 2,000,000원 | 14.0% | 1 |
| 신용대출 | 8,000,000원 | 6.8% | 2 |
| 전세대출 | 80,000,000원 | 4.2% | 3 |

## 4. 투자 및 연금

- 현금 비중: 35%
- 투자 비중: 30%
- 연금 계좌 비중: 20%
- 기타 자산: 15%

## 5. 90일 액션 플랜

### 1개월차

- 지출 기록 시작
- 구독비 정리
- 부채별 금리 확인

### 2개월차

- 고금리 부채 우선 상환
- 비상금 계좌 분리
- ISA/연금저축/IRP 납입 가능 여부 확인

### 3개월차

- 투자 비중 재점검
- 주거 목표 업데이트
- 월간 체크인 실행
```

---

## 한계

이 Skill은 사용자가 입력한 정보에 의존합니다.

따라서 다음과 같은 경우 결과가 부정확할 수 있습니다.

- 입력값이 틀린 경우
- 지출이 누락된 경우
- 부채 금리가 잘못 입력된 경우
- 세금/연금/대출 제도가 최신 정보와 다른 경우
- 사용자의 가족상황, 소득형태, 주거상황이 충분히 반영되지 않은 경우
- 투자 수익률 가정이 실제 시장과 다른 경우

결과는 의사결정의 출발점으로 사용해야 하며, 최종 판단은 사용자 본인의 책임입니다.

---

## 라이선스

이 프로젝트는 MIT License를 따릅니다.  
자세한 내용은 `LICENSE` 파일을 확인하세요.

---

## Attribution

이 프로젝트는 다음 MIT 라이선스 오픈소스 프로젝트의 아이디어와 구조를 참고하여 한국 거주자 기준으로 재구성되었습니다.

### Canadian Personal Finance Manager

Repository: `cjpatten/canadian-finance-planner-skill`  
Copyright (c) 2026 Chris Patten  
License: MIT License

### AI Personal Finance Advisor for Claude Code

Repository: `zubair-trabzada/ai-finance-claude`  
Copyright (c) 2026 Zubair Trabzada  
License: MIT License

이 프로젝트는 원본 프로젝트를 그대로 복사한 것이 아니라, 한국 거주자의 예산, 부채, 투자, 연금, 주거, 세금 체크 흐름에 맞게 재구성한 개인 재무관리 Claude Skill입니다.

---

## Disclaimer

This project is for informational and educational purposes only.

It does not constitute financial, investment, tax, legal, insurance, or accounting advice.  
It does not replace a licensed financial advisor, tax accountant, attorney, insurance planner, or other qualified professional.

All outputs are based on user-provided inputs and assumptions.  
Users are responsible for verifying all information and consulting qualified professionals before making financial decisions.
