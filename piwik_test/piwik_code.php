     /**
     * Visitor ID length
     *
     * @ignore
     */
    const LENGTH_VISITOR_ID = 16;
 
 
 /**
     * Sets the current visitor ID to a random new one.
     */
    public function setNewVisitorId()
    {
        $this->randomVisitorId = substr(md5(uniqid(rand(), true)), 0, self::LENGTH_VISITOR_ID);
        $this->userId = false;
        $this->forcedVisitorId = false;
        $this->cookieVisitorId = false;
    }
