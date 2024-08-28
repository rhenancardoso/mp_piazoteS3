from boot import CONFIG

EMPTY = "No value"

WEB_PAGE_HTML = f"""
<!DOCTYPE html>
<head>
    <style>
        .line{{
            width: 100%;
            height: 0.5rem;
            border-bottom: 0.25rem solid rgb(60, 60, 60);
            border-radius: 0.1rem;
        }}
        td{{
          height: 2rem;
          font-size: 1.15rem;
          border-left: 0.2rem solid rgb(60, 60, 60);
          border-bottom: 0.2rem solid rgb(60, 60, 60);
          border-radius:0.2rem;
          padding-left: 1rem;
        }}
    </style>
    <title>Piazote Storage</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<html>
<body style="background-color:rgb(30, 40, 40); padding: 1.5rem;">
    <h1 style="color:rgb(0, 215, 255); margin: 2rem 1rem 0rem 1rem;">Piazote Storage</h1>
    <div class="line"></div>
    <table style="color:rgb(0, 215, 255); margin: 1rem 1rem 0rem 0rem; width: 100%;">
        <td>1. {CONFIG.ap_words[0] if len(CONFIG.ap_words) > 0 else EMPTY}</td>
        <td>2. {CONFIG.ap_words[1] if len(CONFIG.ap_words) > 1 else EMPTY}</td>
        <td>3. {CONFIG.ap_words[2] if len(CONFIG.ap_words) > 2 else EMPTY}</td>
      </tr>
      <tr>
        <td>4. {CONFIG.ap_words[3] if len(CONFIG.ap_words) > 3 else EMPTY}</td>
        <td>5. {CONFIG.ap_words[4] if len(CONFIG.ap_words) > 4 else EMPTY}</td>
        <td>6. {CONFIG.ap_words[5] if len(CONFIG.ap_words) > 5 else EMPTY}</td>
      </tr>
      <tr>
        <td>7. {CONFIG.ap_words[6] if len(CONFIG.ap_words) > 6 else EMPTY}</td>
        <td>8. {CONFIG.ap_words[7] if len(CONFIG.ap_words) > 7 else EMPTY}</td>
        <td>9. {CONFIG.ap_words[8] if len(CONFIG.ap_words) > 8 else EMPTY}</td>
      </tr>
      <tr>
        <td>10. {CONFIG.ap_words[9] if len(CONFIG.ap_words) > 9 else EMPTY}</td>
        <td>11. {CONFIG.ap_words[10] if len(CONFIG.ap_words) > 10 else EMPTY}</td>
        <td>12. {CONFIG.ap_words[11] if len(CONFIG.ap_words) > 11 else EMPTY}</td>
      </tr>
      <tr>
        <td>13. {CONFIG.ap_words[12] if len(CONFIG.ap_words) > 12 else EMPTY}</td>
        <td>14. {CONFIG.ap_words[13] if len(CONFIG.ap_words) > 13 else EMPTY}</td>
        <td>15. {CONFIG.ap_words[14] if len(CONFIG.ap_words) > 14 else EMPTY}</td>
      </tr>
      <tr>
        <td>16. {CONFIG.ap_words[15] if len(CONFIG.ap_words) > 15 else EMPTY}</td>
        <td>17. {CONFIG.ap_words[16] if len(CONFIG.ap_words) > 16 else EMPTY}</td>
        <td>18. {CONFIG.ap_words[17] if len(CONFIG.ap_words) > 17 else EMPTY}</td>
      </tr>
      <tr>
        <td>19. {CONFIG.ap_words[18] if len(CONFIG.ap_words) > 18 else EMPTY}</td>
        <td>20. {CONFIG.ap_words[19] if len(CONFIG.ap_words) > 19 else EMPTY}</td>
        <td>21. {CONFIG.ap_words[20] if len(CONFIG.ap_words) > 20 else EMPTY}</td>
      </tr>
    </table>
</body>
</html>
"""
