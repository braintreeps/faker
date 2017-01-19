# coding=utf-8

from __future__ import unicode_literals
from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats = (
        '{{first_name}} {{last_name}}',
    )

    first_names = (
        'Erik', 'Maria', 'Karl', 'Margareta', 'Lars', 'Anna', 
         'Nils', 'Kristina', 'Sven', 'Karin', 'Lennart', 'Eva',
        'Anders', 'Birgitta', 'Olof', 'Ingrid', 'Per',  'Johan',
        'Linnéa', 'Åke', 'Kerstin', 'Gustaf', 'Ingeborg', 'Bengt', 'Marianne',
        'Bertil', 'Viola', 'Hans', 'Elsa', 'Jan', 'Inger', 'Arne', 'Lena',
        'Göran', 'Ulla', 'Axel', 'Marie', 'Bo', 'Christina', 'Stig', 'Astrid',
        'John', 'Sofia', 'Gustav', 'Rut', 'Ingemar', 'Viktoria', 'Gösta',
        'Märta', 'Peter', 'Anita', 'Mikael', 'Helena', 'Leif', 'Irene', 'Oskar',
         'Rolf', 'Margit', 'Ingvar', 'Barbro', 'Vilhelm', 'Ingegerd',
        'Kjell', 'Inga', 'Roland', 'Linnea', 'Ulf', 'Britt', 'Rune', 'Signe',
        'Christer', 'Birgit', 'Mats', 'Siv', 'Carl', 'Ester', 'Stefan',
        'Katarina', 'Bror', 'Ingegärd', 'Magnus', 'Matilda', 'Håkan', 'Cecilia',
        'Emanuel',  'Georg', 'Charlotta', 'Fredrik', 'Carina', 'Olov',
         'Kurt', 'Monica', 'Ragnar', 'Susanne', 'Knut', 'Berit', 'Evert',
        'Elin', 'Ivar', 'Sonja', 'Harry', 'Alice', 'Ove', 'Yvonne', 'Björn',
        'Svea', 'Martin', 'Agneta', 'Ernst', 'Greta', 'Einar', 
        'Allan', 'Maj', 'Thomas', 'Edit', 'Folke', 'Annika', 'Valdemar',
         'Birger', 'Karolina', 'Sten',  'Torsten', 'Sigrid',
        'Henry', 'Brita', 'Börje', 'Vilhelmina', 'Robert', 'Ellen', 'Tommy',
        'Johanna', 'Arvid', 'Elvira', 'Harald', 'Ulrika', 'Jonas', 'Anette',
        'Roger', 'Gerd', 'Alf', 'Teresia', 'Sigvard', 'Valborg', 'Helge', 'Ann',
        'Yngve', 'Britta', 'Henrik', 'Maj-Britt', 'Edvin', 'Lilly', 'Tage',
        'Åsa', 'Sture', 'Gertrud', 'Tore', 'Aina', 'Artur', 'Dagmar', 'Kent',
        'Ebba', 'Göte', 'Augusta', 'Emil', 'Emilia', 'Bernt', 'Gudrun', 'Hugo',
        'Gerda', 'Hjalmar', 'Solveig', 'Jörgen', 'Agnes', 'Albert', 'Lovisa',
        'Holger', 'Louise', 'Inge', 'Lisa', 'Adolf', 'Josefina', 'Kenneth',
        'Mona', 'Tomas', 'Ruth', 'Verner', 'Hanna', 'Torbjörn', 'Jenny', 'Ture',
        'Eleonora', 'Sune', 'Ragnhild', 'August', 'Lilian', 'Valter', 'Eivor',
        'Uno', 'Hildur', 'Viktor',   'Stina', 'David',
        'Monika', 'Sigfrid', 'Dagny', 'Otto', 'Helga', 'Edvard', 'Britt-Marie',
        'Alfred', 'Pia', 'Sören', 'Hilda', 'Paul', 'Olga', 'Sixten', 'Ingela',
        'Patrik', 'Ida', 'Hilding', 'Anneli', 'Henning', 'Berta', 'Bernhard',
        'Emma', 'Klas', 'Margaretha', 'Reinhold', 'Marita', 'Krister',
        'Camilla', 'Sigurd', 'Ann-Marie', 'Algot', 'Mary', 'Ivan', 'Alma',
        'Michael', 'Hulda', 'Rudolf', 'Vera', 'Erland', 'Charlotte', 'Albin',
        'Maud', 'Helmer', 'Iris', 'Claes', 'Asta', 'Herman', 'Olivia', 'Alvar',
        'Evy', 'Dan', 'Inga-Lill', 'Gerhard', 'Doris', 'Johannes', 'Ulla-Britt',
        'Evald', 'Helen', 'Gottfrid', 'Erika', 'Ola', 'Hilma', 'Eric', 'Sylvia',
        'Rickard', 'Sara', 'Daniel', 'Hildegard', 'Arnold', 'Frideborg',
        'Frans', 'Irma', 'Mauritz', 'Helene', 'Gert', 'Tyra', 'Valfrid', 'Inez',
        'Teodor', 'Harriet', 'Conny', 'Ottilia', 'Fritz', 'Elna', 'Wilhelm',
        'Amalia', 'Olle', 'Laila', 'Anton', 'Ella', 'Urban', 'Anne', 'Valentin',
        'Annie', 'Josef', 'Lillemor', 'Elof', 'Eugenia', 'William', 'Elsie',
        'Leonard', 'Klara', 'Tord', 'Hillevi', 'Egon', 'Marta', 'Joakim',
        'Iréne', 'Erling', 'Mari', 'Staffan', 'Hedvig', 'Elis', 'Selma',
        'Ronny', 'Anne-Marie', 'Andreas', 'Ann-Christin', 'Mattias',
        'Ann-Charlotte', 'Bert', 'Marie-Louise', 'Eskil', 'Anna-Lisa',
        'Alexander', 'Agda', 'Julius', 'Jeanette', 'Ingmar', 'Malin',
        'Christian', 'Siri', 'Ferdinand', 'Alfrida', 'Jonny', 'Ann-Mari',
        'Benny', 'Frida', 'Richard', 'Majken', 'Jan-Erik', 'Rose-Marie',
        'Lars-Erik', 'Elise', 'Konrad', 'Ingalill', 'Natanael', 'Annette',
        'Ludvig', 'Göta', 'Niklas', 'Paulina', 'Tony', 'Amanda', 'Johnny',
         'Eugen', 'Alfhild', 'Pär', 'Gulli', 'Morgan', 'Judit',
        'Svante', 'Evelina', 'Fritiof', 'Pernilla', 'Östen', 'Inga-Britt',
        'Karl-Erik', 'Anna-Lena', 'Agne', 'Hjördis', 'Oscar', 'Ann-Britt',
        'Kristian', 'Fredrika', 'Jens', 'Carin', 'Filip', 'Elsy', 'Manfred',
        'Magdalena', 'Curt', 'Mariana', 'Samuel', 'Margot'
    )

    last_names = (
        'Johansson', 'Andersson', 'Karlsson', 'Nilsson', 'Eriksson', 'Larsson',
        'Olsson', 'Persson', 'Svensson', 'Pettersson', 'Gustafsson', 'Jonsson',
        'Jansson', 'Hansson', 'Jönsson', 'Petersson', 'Bengtsson', 'Carlsson',
        'Gustavsson', 'Magnusson', 'Olofsson', 'Lindberg', 'Lindström',
        'Jakobsson', 'Lindgren', 'Axelsson', 'Lundberg', 'Bergström',
        'Lundgren', 'Fredriksson', 'Mattsson', 'Berglund', 'Berg', 'Henriksson',
        'Sandberg', 'Håkansson', 'Danielsson', 'Lindqvist', 'Fransson',
        'Sjöberg', 'Forsberg', 'Johnsson', 'Engström', 'Samuelsson', 'Lundin',
        'Eklund', 'Lind', 'Mårtensson', 'Holm', 'Lundqvist', 'Nyström',
        'Holmberg', 'Isaksson', 'Bergman', 'Söderberg', 'Nordström', 'Nyberg',
        'Eliasson', 'Lundström', 'Björk', 'Arvidsson',  'Ström',
        'Berggren', 'Månsson', 'Wallin', 'Hermansson', 'Nordin', 'Björklund',
        'Jonasson', 'Andreasson', 'Sundberg', 'Hedlund', 'Sandström', 'Ekström',
        'Holmgren', 'Sjögren', 'Åberg', 'Abrahamsson', 'Öberg', 'Göransson',
        'Hellström', 'Martinsson', 'Strömberg', 'Blom', 'Dahlberg', 'Norberg',
        'Söderström', 'Blomqvist', 'Sundström', 'Löfgren', 'Åkesson', 'Åström',
        'Johannesson', 'Bergqvist', 'Josefsson', 'Ek', 'Adolfsson', 'Börjesson',
        'Lund', 'Ottosson', 'Hallberg', 'Boström', 'Englund', 'Lindholm',
        'Möller', 'Nyman', 'Nygren', 'Palm', 'Sjöström', 'Dahl', 'Viklund',
        'Söderlund', 'Borg', 'Falk', 'Ivarsson', 'Höglund', 'Vikström',
        'Holmström', 'Hedberg', 'Bäckström', 'Davidsson', 'Aronsson', 'Pålsson',
        'Friberg', 'Lindblom', 'Skoglund', 'Björkman', 'Östlund', 'Ekman',
        'Lindahl', 'Strandberg', 'Olausson', 'Rosén', 'Erlandsson', 'Strand',
        'Stenberg', 'Edlund', 'Klasson', 'Haglund', 'Augustsson', 'Holmqvist',
        'Dahlgren', 'Oskarsson', 'Knutsson', 'Moberg', 'Malm', 'Norén',
        'Högberg', 'Dahlström', 'Sundqvist', 'Sundin', 'Von', 'Hedström',
        'Blomberg', 'Franzén', 'Lindén', 'Melin', 'Claesson', 'Alm', 'Boman',
        'Nord', 'Paulsson', 'Sjödin', 'Hedman', 'Kristiansson', 'Wikström',
        'Näslund', 'Berntsson', 'Öhman', 'Lundmark', 'Hagström', 'Ågren',
        'Lindell', 'Molin', 'Roos', 'Lindkvist', 'Lundkvist', 'Svärd', 'Sköld',
        'Ljungberg', 'Lilja', 'Ståhl', 'Lindblad', 'Ericsson', 'Norman',
        'Hellberg', 'Ohlsson', 'Niklasson', 'Ekberg', 'Ljung', 'Alfredsson',
        'Österberg', 'Malmberg', 'Törnqvist', 'Forslund', 'Hedin', 'Edström',
        'Linder', 'Frisk', 'Wahlström', 'Hägglund', 'Skog', 'Bäckman',
        'Emanuelsson', 'Asplund', 'Byström', 'Ahlström', 'Lövgren', 'Marklund',
        'Dahlin', 'Hagberg', 'Simonsson', 'Fors', 'Nordlund', 'Nordqvist',
        'Alexandersson', 'Ljunggren', 'Edvardsson', 'Karlström', 'Brandt',
        'Jacobsson', 'Antonsson', 'Bergkvist', 'Hjalmarsson', 'Ahlberg',
        'Dahlqvist', 'Hjelm', 'Hall', 'Malmström', 'Vilhelmsson', 'Backman',
        'Grahn', 'Wiklund', 'Lindvall', 'Salomonsson', 'Westerberg',
        'Kjellberg', 'Vallin', 'Backlund', 'Östman', 'Vesterlund', 'Westerlund',
        'Granberg', 'Strid', 'Jensen', 'Forsman', 'Torstensson', 'Hult',
        'Hallgren', 'Hellman', 'Almqvist', 'Kristensson', 'Levin', 'Sjöblom',
        'Rydberg', 'Svedberg', 'Jeppsson', 'Hellgren', 'Viberg', 'Ahlgren',
        'Sjöholm', 'Palmqvist', 'Hagman', 'Hägg', 'Kvist', 'Blomgren',
        'Östberg', 'Gabrielsson', 'Israelsson', 'Kristoffersson', 'Wiberg',
        'Malmqvist', 'Vestin', 'Sandin', 'Engman', 'Lundell', 'Westman',
        'Nordgren', 'Broberg', 'Hultgren', 'Rydén', 'Sjöstrand', 'Malmgren',
        'Hansen', 'Lindh', 'Rosengren', 'Bäck', 'Åkerlund', 'Sahlin', 'Hultman',
        'Engberg', 'Holgersson', 'Karlberg', 'Ekholm', 'Lindmark', 'Hallin',
        'Hammar', 'Broman', 'Gren', 'Hammarström', 'Krantz', 'Bertilsson',
        'Svanberg', 'Norling', 'Asp', 'Nylander', 'Bodin', 'Sandgren',
        'Brännström', 'Nielsen', 'Svantesson', 'Svahn', 'Blomkvist', 'Thorén',
        'Ekstrand', 'Bolin', 'Wahlberg', 'Lantz', 'Löf', 'Söderqvist',
        'Westberg', 'Sjölund', 'Andrén', 'Engdahl', 'Ekelund', 'Norrman',
        'Halvarsson', 'Forsgren', 'Henningsson', 'Lindskog', 'Norgren',
        'Granström', 'Nordberg', 'Burman', 'Borgström', 'Vestman', 'Söderholm',
        'Westin', 'Melander', 'Sjöstedt', 'Åsberg', 'Sandell', 'Häggström',
        'Bylund', 'Södergren', 'Lundblad', 'Åslund', 'Elofsson', 'Öman',
        'Haraldsson', 'Forsell', 'Sjölin', 'Lindquist', 'Östling', 'Almgren',
        'Källström', 'Brodin', 'Eklöf', 'Lidén', 'Ahlqvist', 'Lennartsson',
        'Ljungqvist', 'Wall', 'Blixt', 'Landin', 'Rasmusson', 'Thulin',
        'Granlund', 'Nylén', 'Ögren', 'Söderman', 'Lundquist', 'Helgesson',
        'Bohlin', 'Palmgren', 'Kling', 'Nordlander', 'Lindfors', 'Linde',
        'Edman', 'Frank', 'Frid', 'Norlin', 'Flink', 'Ekdahl', 'Bergvall',
        'Rosenqvist', 'Flodin', 'Lundholm', 'Turesson', 'Sundell', 'Robertsson',
        'Sjölander', 'Lundh', 'Lundahl', 'Landström', 'Engvall', 'Bergsten',
        'Ericson', 'Pedersen', 'Zetterberg', 'Widén', 'Liljegren', 'Ahlin',
        'Vestlund', 'Edin', 'Lönn', 'Vestberg', 'Nyqvist', 'Stenström', 'Stark',
        'Wennberg', 'Lidström', 'Brolin', 'Anderberg', 'Sundkvist', 'Matsson',
        'Vesterberg', 'Edberg', 'Skoog', 'Bergstrand', 'Ring', 'Norström',
        'Pihl', 'Olander', 'Stenlund', 'Granath', 'Åman', 'Hjort', 'Åkerström',
        'Werner', 'Hultberg', 'Sten', 'Emilsson', 'Christensson', 'Olovsson',
        'Wahlgren', 'Wester', 'Österlund', 'Holst', 'Högström', 'Roth',
        'Albertsson', 'Grönlund', 'Ahl', 'Einarsson', 'Rask', 'Klang',
        'Westlund', 'Norin', 'Gullberg', 'Fagerström', 'Green', 'Dahlén',
        'Ferm', 'Enström', 'Broström', 'Holmkvist', 'Fält', 'Hallström',
        'Adamsson', 'Åkerman', 'Söder', 'Sjöqvist', 'Viktorsson', 'Åkerblom',
        'Svanström', 'Rehn', 'Holmlund', 'Olin', 'Boberg', 'Rylander',
        'Sandqvist', 'Juhlin', 'Bäcklund', 'Selin', 'Zetterström', 'Wallén',
        'Storm', 'Thunberg', 'Ekvall', 'Hellqvist', 'Molander', 'Lindman',
        'Lindeberg', 'Rundqvist', 'Nordén', 'Törnblom', 'Risberg', 'Brink',
        'Wallgren', 'Bohman', 'Grönberg', 'Åkerberg', 'Bergdahl', 'Modig',
        'Albinsson', 'Östergren', 'Edvinsson'
    )
