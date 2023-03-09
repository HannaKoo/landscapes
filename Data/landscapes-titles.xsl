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
<!-- Remember to remove <note> -->
    <p>
      <xsl:value-of select="edition/title" />
    </p>
  </xsl:for-each>
  
</body>
</html>
</xsl:template>
</xsl:stylesheet>
