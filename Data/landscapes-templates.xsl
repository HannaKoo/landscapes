<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
<html>
<body>
  <xsl:apply-templates select="landscapes/document" />
</body>
</html>
</xsl:template>

<xsl:template match="landscapes/document">
  <xsl:apply-templates select="regesta"/>
  <xsl:apply-templates select="edition"/>
</xsl:template>

<xsl:template match="regesta">
  <p><xsl:value-of select="."/></p>
</xsl:template>

<xsl:template match="edition">
  <blockquote>
    <xsl:value-of select="."/>
  </blockquote>
  <xsl:apply-templates select="landscape"/>
</xsl:template>

<xsl:template match="landscape">
  <strong><xsl:value-of select="."/></strong>
</xsl:template>



  <!-- <xsl:for-each select="landscapes/document">
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
      <h3>
        <xsl:value-of select="title" />
      </h3>
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
  </xsl:for-each> -->
  
</xsl:stylesheet>
