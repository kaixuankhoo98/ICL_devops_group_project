database = {"shakespeare":
            "William Shakespeare (26 April 1564 - 23 April 1616) was an\n"
            "English poet, playwright, and actor, widely regarded as the\n"
            "greatest writer in the English language and the world's\n"
            "pre-eminent dramatist.",
            "asimov":
            "Isaac Asimov (2 January 1920 - 6 April 1992) was an\n"
            "American writer and professor of Biochemistry, famous for\n"
            "his works of hard science fiction and popular science.",
            "einstein":
            "Albert Einstein (14 March 1879 - 18 April 1965) was a\n"
            "a German-born theoretical physicist, widely acknowledged to\n"
            " be one of the greatest physicists of all time. Einstein is\n"
            "best known for developing the theory of relativity, but he\n" 
            "also made important contributions to the development of the theory of quantum mechanics.",
            "wollstonecraft":
            "Mary Wollstonecraft (27 April 1759 - 10 September 1797) was an \n"
            "English writer, philosopher, and advocate of women's rights. Until the\n"
            " late 20th century, Wollstonecraft's life, which encompassed several unconventional\n"
            " personal relationships at the time, received more attention than her writing.",
            "shelley":
            "Mary Wollstonecraft Shelley (30 August 1797 - 1 February 1851) was an\n" 
            "English novelist who wrote the Gothic novel Frankenstein; or, The Modern Prometheus,\n"
            " which is considered an early example of science fiction. She also edited and promoted \n"
            "the works of her husband, the Romantic poet and philosopher Percy Bysshe Shelley.",

            }


def process(query):
    return [val for key, val in database.items() if key in query.lower()]
