<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
      xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:output method="html" encoding="UTF-8" indent="yes"/>

  <!-- Plantilla raíz -->
  <xsl:template match="/">
    <html>
      <head>
        <title>Blog con plantillas</title>
        <style>
          body { font-family: Arial; padding: 2em; background: #f4f4f4; }
          .post { background: white; padding: 1em; margin-bottom: 1em; border-radius: 5px; border: 1px solid #ddd; }
          .meta, .categorias { font-size: 0.9em; color: #666; }
        </style>
      </head>
      <body>
        <h1>Blog con plantillas</h1>
        <xsl:apply-templates select="blog/post"/>
      </body>
    </html>
  </xsl:template>

  <!-- Plantilla para cada post -->
  <xsl:template match="post">
    <div class="post">
      <h2><xsl:value-of select="titulo"/></h2>
      <div class="meta">Por <strong><xsl:value-of select="autor"/></strong> el <xsl:value-of select="fecha"/></div>
      <div class="categorias">
        Categorías:
        <xsl:apply-templates select="categorias/categoria"/>
      </div>
      <p><xsl:value-of select="contenido"/></p>
    </div>
  </xsl:template>

  <!-- Plantilla para una categoría -->
  <xsl:template match="categoria">
    <xsl:value-of select="."/>
    <xsl:if test="position() != last()">, </xsl:if>
  </xsl:template>

</xsl:stylesheet>

