$(function(){
  // 현재 페이지 파일명
  const currentPath = location.pathname.split("/").pop(); // 예: html_rule.html
  const currentHash = location.hash; // 예: #html_rule

  // ✅ index.html이면 on/off 처리 전부 생략
  if (currentPath === '' || currentPath === 'index.html') {
    return; // 이 아래 코드는 실행되지 않음
  }

  // ✅ GNB 활성화 규칙 (파일명 포함 조건)
  if (currentPath.includes('coding')) {
    $('.gnb li:eq(0)').addClass('on'); // 개요
  } else if (currentPath.includes('chtml')) {
    $('.gnb li:eq(1)').addClass('on'); // HTML
  } else if (currentPath.includes('css')) {
    $('.gnb li:eq(2)').addClass('on'); // CSS
  }

  // ✅ on이 없는 li에 off 추가
  $('.gnb li').each(function(){
    if (!$(this).hasClass('on')) {
      $(this).addClass('off');
    }
  });
});
