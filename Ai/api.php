<?php
// api.php

$data = json_decode(file_get_contents("php://input"), true);
$input = $data["input"];

// 규칙 파일 로드
$rules = file_get_contents("gpt_rules.html");

$prompt = $rules . "\n\n" . $input;

$apiKey = "YOUR_OPENAI_API_KEY";

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, "https://api.openai.com/v1/chat/completions");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);

curl_setopt($ch, CURLOPT_HTTPHEADER, [
  "Content-Type: application/json",
  "Authorization: Bearer " . $apiKey
]);

curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode([
  "model" => "gpt-4o-mini",
  "messages" => [
    ["role" => "user", "content" => $prompt]
  ]
]));

$response = curl_exec($ch);
curl_close($ch);

$result = json_decode($response, true);

echo $result["choices"][0]["message"]["content"];
?>