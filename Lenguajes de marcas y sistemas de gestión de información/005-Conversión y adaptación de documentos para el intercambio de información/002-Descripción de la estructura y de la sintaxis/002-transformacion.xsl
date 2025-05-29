<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
      xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:output method="html" encoding="UTF-8" indent="yes"/>

  <xsl:template match="/">
    <html>
      <head>
        <title>Blog generado desde XML</title>
        <style>
          body { font-family: Arial; padding: 2em; background: #f8f8f8; }
          .post { background: #fff; border: 1px solid #ccc; padding: 1em; margin-bottom: 1em; border-radius: 5px; }
          h2 { margin-top: 0; }
          .meta { font-size: 0.9em; color: #666; margin-bottom: 0.5em; }
          .categorias { font-size: 0.85em; color: #444; }
        </style>
      </head>
      <body>
        <h1>Blog generado desde XML</h1>
        <xsl:for-each select="blog/post">
          <div class="post">
            <h2><xsl:value-of select="titulo"/></h2>
            <div class="meta">
              Por <strong><xsl:value-of select="autor"/></strong> el <xsl:value-of select="fecha"/>
            </div>
            <div class="categorias">
              Categorías:
              <xsl:for-each select="categorias/categoria">
                <xsl:value-of select="."/>
                <xsl:if test="position() != last()">, </xsl:if>
              </xsl:for-each>
            </div>
            <p><xsl:value-of select="contenido"/></p>
          </div>
        </xsl:for-each>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>

