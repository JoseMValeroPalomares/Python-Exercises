import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuración del servidor SMTP
smtp_server = 'smtp.tudominio.com'
smtp_port = 587
smtp_username = 'tucorreo@tudominio.com'
smtp_password = 'tucontraseña'

# Configuración del remitente y destinatario
from_address = 'josevaleropalomares@gmail.com'
to_address = 'josevaleropalomares@gmail.com'

# Crear el mensaje Multipart
message = MIMEMultipart()
message['From'] = from_address
message['To'] = to_address
message['Subject'] = 'Asunto del correo'

# Contenido HTML del correo
html_content = """
<html>
  <body>
    <h2>¡Hola!</h2>
    <p>Este es un correo de ejemplo con <strong>contenido HTML</strong>.</p>
    <p>Puedes personalizar este contenido como desees.</p>
    <p><a href="https://www.ejemplo.com">Visita nuestro sitio web</a></p>
  </body>
</html>
"""

# Adjuntar el contenido HTML al mensaje
message.attach(MIMEText(html_content, 'html'))

# Iniciar la conexión con el servidor SMTP
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Enviar el correo electrónico
    server.sendmail(from_address, to_address, message.as_string())

print("Correo enviado con éxito.")
