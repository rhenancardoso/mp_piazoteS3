import secret

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
      <tr>
      <tr>
        <td>1. {secret.WORD01}</td>
        <td>2. {secret.WORD02}</td>
        <td>3. {secret.WORD03}</td>
      </tr>
      <tr>
        <td>4. {secret.WORD04}</td>
        <td>5. {secret.WORD05}</td>
        <td>6. {secret.WORD06}</td>
      </tr>
      <tr>
        <td>7. {secret.WORD07}</td>
        <td>8. {secret.WORD08}</td>
        <td>9. {secret.WORD09}</td>
      </tr>
      <tr>
        <td>10. {secret.WORD10}</td>
        <td>11. {secret.WORD11}</td>
        <td>12. {secret.WORD12}</td>
      </tr>
      <tr>
        <td>13. {secret.WORD13}</td>
        <td>14. {secret.WORD14}</td>
        <td>15. {secret.WORD15}</td>
      </tr>
      <tr>
        <td>16. {secret.WORD16}</td>
        <td>17. {secret.WORD17}</td>
        <td>18. {secret.WORD18}</td>
      </tr>
      <tr>
        <td>19. {secret.WORD19}</td>
        <td>20. {secret.WORD20}</td>
        <td>21. {secret.WORD21}</td>
      </tr>
    </table>
</body>
</html>
"""
