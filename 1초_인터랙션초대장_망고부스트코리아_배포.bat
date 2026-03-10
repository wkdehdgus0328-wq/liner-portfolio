@echo off
chcp 65001 > nul
echo ========================================================
echo   망고부스트코리아 인터랙션 초대장 포트폴리오 1초 배포 스크립트
echo ========================================================
echo.

cd /d "C:\Users\cob\Desktop\취업자료26\지원서\망고부스트코리아 지원서\인터렉션 초대장 망고부스트코리아"

echo [1/3] 기존 빌드 파일(dist) 삭제 중...
if exist dist rmdir /s /q dist

echo [2/3] 프로젝트 빌드 진행 중...
call npm run build
if %errorlevel% neq 0 (
    echo [에러] 빌드 중 오류가 발생했습니다.
    pause
    exit /b %errorlevel%
)

echo [3/3] GitHub Pages(master)로 배포 중...
cd dist
call git init
call git add .
call git commit -m "Deploy Invite"
call git branch -M master
call git remote add origin https://github.com/wkdehdgus0328-wq/mangoboost-invite.git
call git push -f origin master
if %errorlevel% neq 0 (
    echo [에러] 배포 중 오류가 발생했습니다.
    cd ..
    pause
    exit /b %errorlevel%
)
cd ..

echo.
echo ========================================================
echo   배포가 성공적으로 완료되었습니다!
echo   약 1~2분 뒤 반영됩니다.
echo   URL: https://wkdehdgus0328-wq.github.io/mangoboost-invite/
echo ========================================================
pause
