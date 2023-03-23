<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
<html>
<body>

  <xsl:for-each select="landscapes/document">
    <h2>
      <xsl:value-of select="@nr"/>
      <xsl:text>. </xsl:text>
      <xsl:value-of select="@when"/>
      <xsl:text> </xsl:text>
      <i><xsl:value-of select="@where"/></i>
    </h2>
    <xsl:for-each select="regesta">
      <blockquote>
        <xsl:value-of select=".">
          <strong>
            <xsl:value-of select="landscape"/>
          </strong>
        </xsl:value-of>
      </blockquote>
    </xsl:for-each>
    <xsl:for-each select="edition">
      <p>
        <xsl:value-of select=".">
          <xsl:for-each select="landscape">
            <strong>
              <xsl:value-of select="."/>
            </strong>
          </xsl:for-each>
       </xsl:value-of>
      </p>
    </xsl:for-each>
  </xsl:for-each>
  
</body>
</html>
</xsl:template>
</xsl:stylesheet>
