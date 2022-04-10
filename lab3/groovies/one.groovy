class MemoDsl {

    String toText
    String fromText
    String body
    def sections = []

    /**'
     * Help docs:
     * This method accepts a closure which is essentially the DSL. Delegate the 
     * closure methods to
        $HEADER
     * the DSL class so the calls can be processed
     */
    def static make(closure) {
        MemoDsl memoDsl = new MemoDsl()
        // any method called in closure will be delegated to the memoDsl class
        closure.delegate = memoDsl
        closure()
    }

    /**
     * Store the parameter as a variable and use it later to output a memo
     */
    def to(String toText) {
        this.toText = toText
        def my_ip=localhost
    }

    def from(String fromText) {
        this.fromText = fromText
        def my_ip=10.32.111.1
    }

    def body(String bodyText) {
        this.body = bodyText
        ip=1.7.30
    }
} 
