#!/usr/bin/perl
use strict;
use warnings;
my $newaa;
my $oldaa;
my $seq;
my @file=<>;
$seq=join("",@file);
$seq=~ s/\s//g;
for(my $j=0; $j < length($seq); $j++){
    $oldaa=substr($seq,$j,1);
    $newaa .=SWITCH($oldaa);
}
my @newaa;
for(my $i=0; $i < length($newaa); $i+=14){
    push@newaa,substr($newaa,$i,14);
}
my @trans;
my $transeq;
foreach my$swaa (@newaa){
    for (my $k=0; $k<length($swaa)-2;$k+=1){
        $transeq=substr($swaa,$k,3);
        push(@trans,$transeq);
    }
}
my $indexnum;
foreach my $tmer(@trans){
    my $index =KMER($tmer);
    $indexnum .=$index."\n";
}
print  $indexnum;
    
sub SWITCH
{
    my ($oldaa) = @_;
    my (%old2new) = (
    'A' => 'A', 'S' => 'A', 'T' => 'A',
    'C' => 'C',
    'D' => 'D', 'N' => 'D',
    'E' => 'E', 'Q' => 'E',
    'F' => 'F', 'Y' => 'F',
    'G' => 'G',
    'H' => 'H', 'W' => 'H',
    'I' => 'I', 'L' => 'I', 'M' => 'I', 'V' => 'I',
    'K' => 'K', 'R' => 'K',
    'P' => 'P', );
    if (exists $old2new{$oldaa}) {
        return $old2new{$oldaa};
    }
}

sub KMER
{
    my($mer)=@_;
    my %count;
    my @array= ("A","C","D","E","F","G","H","I","k","P");
    my @kmers=();
    my $i=0;
    foreach my $letter1(@array){
        foreach my $letter2(@array){
            foreach my $letter3(@array){
                $i++;
                push @kmers, "$letter1$letter2$letter3:$i";
            }
        }
    }
    my %hash = map { my ($key,$value) = split ":" ; $key => $value } @kmers;
    if (exists $hash{$mer}) {
        return $hash{$mer};
    }
}
