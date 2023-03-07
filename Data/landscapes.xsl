<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
<html>
<body>
  <xsl:for-each select="landscapes/document">
    <h2>
      <xsl:value-of select="@nr"/>:
      <xsl:value-of select="@when"/>,
      <xsl:value-of select="@where"/>
    </h2>
    <blockquote>
      <xsl:value-of select="regesta" />
      <strong>
        <xsl:value-of select="landscapes/document/edition/landscape"/>
      </strong>
    </blockquote>
    <p>
      <xsl:value-of select="edition" />
      <strong>
        <xsl:value-of select="landscape"/>
      </strong>
    </p>
  </xsl:for-each>
  <div>
  </div>

  
</body>
</html>
</xsl:template>
</xsl:stylesheet>
